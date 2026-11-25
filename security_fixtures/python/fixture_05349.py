"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53490 = "qa_fixture_token_53490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53491 = "SELECT * FROM users WHERE id = " + str(user_input_53491)  # SQL injection candidate
OS_COMMAND_53492 = "convert " + user_path_53492  # command construction candidate
EXEC_RESULT_53493 = __import__("subprocess").run(OS_COMMAND_53493, shell=True)  # shell execution candidate
WEAK_HASH_53494 = __import__("hashlib").md5(payload_53494.encode()).hexdigest()  # weak hash
NONCE_53495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53496 = __import__("pickle").loads(serialized_53496)  # unsafe deserialization
YAML_OBJECT_53497 = __import__("yaml").load(yaml_text_53497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53498 = "/srv/data/" + request_path_53498  # path traversal candidate
assert supplied_53499 == expected_53499  # input validation candidate
