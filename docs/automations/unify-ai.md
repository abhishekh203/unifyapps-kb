# Agentic AI Platform for the Enterprise

Source: https://www.unifyapps.com/docs/unify-automations/unify-ai
Section: automations

---

## Overview

Unify AI provides comprehensive artificial intelligence and machine learning capabilities for your automation workflows. This enables you to process documents, extract embeddings, perform image operations, fine-tune models, and transform code structures, making it essential for AI-powered document processing, computer vision tasks, and intelligent data analysis.

## Read PDF File Pages

This action processes PDF documents for content extraction and analysis, enabling automated document workflow processing. Add the Unify AI node, select "`Read PDF File Pages`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. PDF file identification and processing parameters are handled through workflow context and file upload mechanisms.

**Output:** Returns processed PDF page information, including extracted text content, page metadata, structural information, and formatting details that can be used in subsequent document analysis and content processing workflows.

## Read File

This action processes unstructured files for content extraction, supporting various file formats beyond PDFs. Add the Unify AI node, select "`Read File`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. File type detection and content extraction parameters are managed automatically through the workflow context.

**Output:** Returns processed file content information, including extracted text, file metadata, content structure, and format-specific details that enable comprehensive document processing and analysis workflows.

## Read File (Docling)

This action uses the Docling framework for advanced document processing, providing enhanced document understanding capabilities. Add the Unify AI node, select "`Read File (Docling)`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Docling framework parameters and document processing configurations are handled through workflow automation settings.

**Output:** Returns processed document information using Docling framework, including structured content extraction, semantic understanding, enhanced metadata, and document intelligence features that support advanced document workflow automation.

## Chunk File (Docling)

This action breaks documents into smaller, manageable chunks using Docling technology, enabling efficient processing of large documents. Add the Unify AI node, select "`Chunk File (Docling)`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Chunking parameters including chunk size, overlap settings, and content boundaries are configured through workflow automation.

**Output:** Returns chunked document segments with metadata, including chunk boundaries, content preservation details, reference links between chunks, and segmentation quality metrics that enable efficient large document processing workflows.

## Chunk Files (Docling) (Batch)

This action processes multiple files simultaneously for chunking operations, enabling high-throughput document processing workflows. Add the Unify AI node, select "`Chunk Files (Docling) (Batch)`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Batch processing parameters including file queue management and parallel processing settings are handled through workflow configuration.

**Output:** Returns batch-processed chunked content with comprehensive results, including per-file chunking status, aggregated processing metrics, error handling details, and batch completion information for scalable document processing operations.

## Text Splitter

This action divides text into segments using advanced chunking algorithms with embedding-based intelligent splitting. Add the Unify AI node, select "`Text Splitter`" option and provide below mentioned inputs.

**Inputs:**

- **Embedding Type:** Set to "`HUGGING_FACE`" (specifies the embedding framework used for semantic text understanding during splitting)
- **Embedding Model:** Set to "`sentence-transformers/all-mpnet-base-v2`" (defines the specific pre-trained model for generating text embeddings)
- **Threshold Type:** Set to "`percentile`" (determines the statistical method used for establishing splitting criteria based on semantic similarity)

**Output:** Returns segmented text with embedding-based splitting results, including semantic chunk boundaries, similarity scores between segments, embedding vectors for each chunk, and splitting quality metrics that enable intelligent text processing and retrieval workflows.

## Model Fine Tuning Job

This action schedules and manages model training processes, enabling automated machine learning workflow execution. Add the Unify AI node, select "`Model Fine Tuning Job`" option and provide below mentioned inputs.

**Inputs:**

- **Interval:** Set to 5 (frequency value for job execution, controlling how often the fine-tuning process checks for updates or iterations)
- **Frequency:** Set to "`MINUTES`" (time unit for interval specification, defining the temporal granularity of job scheduling)

**Output:** Returns fine-tuning job status and details, including training progress metrics, model performance indicators, resource utilization data, and completion estimates that enable monitoring and management of machine learning training workflows.

## Deploy Fine Tuned Model

This action makes trained models available for inference, transitioning models from training to production environments. Add the Unify AI node, select "`Deploy Fine Tuned Model`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Model deployment parameters including scaling settings and endpoint configuration are managed through workflow automation.

**Output:** Returns deployment status and model information, including endpoint URLs, model versioning details, performance benchmarks, and availability status that enable integration of trained models into production workflows and applications.

## Extract Face Embedding

This action generates facial recognition embeddings from images, enabling biometric identification and analysis workflows. Add the Unify AI node, select "`Extract Face Embedding`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Image processing parameters and face detection settings are handled automatically through the workflow context.

**Output:** Returns face embedding vectors and metadata, including numerical face representations, detection confidence scores, facial landmark information, and quality assessments that enable facial recognition, comparison, and identity verification workflows.

## Image Converter

This action transforms images between different formats and performs image processing operations for workflow compatibility. Add the Unify AI node, select "`Image Converter`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Image conversion parameters including target formats, quality settings, and processing options are configured through workflow automation.

**Output:** Returns converted image information, including format conversion results, image quality metrics, file size optimizations, and processing metadata that enable seamless image workflow integration and format standardization.

## Identify and Normalize Time Expressions

This action processes text to extract and standardize temporal information, enabling automated time-based data processing. Add the Unify AI node, select "`Identify and Normalize Time Expressions`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Text processing parameters and temporal extraction rules are managed through workflow configuration and natural language processing settings.

**Output:** Returns normalized time expressions and temporal data, including standardized date formats, time zone conversions, relative time calculations, and temporal relationship metadata that enable time-sensitive workflow automation and scheduling operations.

## Transform Python Code to Graph

This action converts Python source code into graph representations for analysis, enabling code structure visualization and dependency mapping. Add the Unify AI node, select "`Transform Python Code to Graph`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Code analysis parameters including parsing depth and graph generation settings are handled through workflow automation configuration.

**Output:** Returns graph structure representing Python code relationships, including function dependencies, class hierarchies, import relationships, and code complexity metrics that enable automated code review, refactoring, and architectural analysis workflows.

## Transform Java Code to Graph

This action converts Java source code into graph representations for analysis, providing comprehensive code structure understanding. Add the Unify AI node, select "`Transform Java Code to Graph`" option and provide below mentioned inputs.

**Inputs:** No specific input fields are defined for this action. Java-specific parsing parameters and graph generation configurations are managed automatically through workflow settings.

**Output:** Returns graph structure representing Java code relationships, including package dependencies, class inheritance hierarchies, method call graphs, and architectural patterns that enable enterprise-level code analysis and software engineering workflow automation.

## Use Cases

**Intelligent Document Processing:** Organizations can automate document analysis workflows by reading files, chunking content, and extracting structured information from various document formats including PDFs and unstructured files. For example, a legal firm could use Read PDF File Pages to extract contract content, Chunk File (Docling) to break documents into manageable sections, Text Splitter to create semantically meaningful segments, and Identify and Normalize Time Expressions to extract important dates and deadlines for automated contract management and compliance tracking.

**Machine Learning Model Management:** Data science teams can automate model fine-tuning processes, deploy trained models, and manage machine learning workflows at scale. A recommendation system team might use Model Fine Tuning Job to continuously retrain models with new user data every 5 minutes, Deploy Fine Tuned Model to push updated models to production endpoints, and Extract Face Embedding for user profile image processing, creating an end-to-end automated ML pipeline that adapts to changing user preferences.

**Code Analysis and Transformation:** Development teams can analyze codebases by transforming Python and Java code into graph representations for better understanding of code structure and dependencies. A software architecture team could use Transform Python Code to Graph and Transform Java Code to Graph to analyze microservices dependencies, identify code complexity hotspots, detect circular dependencies, and automate code review processes for large-scale enterprise applications with multiple programming languages.
