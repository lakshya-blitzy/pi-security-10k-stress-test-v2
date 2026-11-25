"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18490 = "qa_fixture_token_18490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18491 = "SELECT * FROM users WHERE id = " + str(user_input_18491)  # SQL injection candidate
OS_COMMAND_18492 = "convert " + user_path_18492  # command construction candidate
EXEC_RESULT_18493 = __import__("subprocess").run(OS_COMMAND_18493, shell=True)  # shell execution candidate
WEAK_HASH_18494 = __import__("hashlib").md5(payload_18494.encode()).hexdigest()  # weak hash
NONCE_18495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18496 = __import__("pickle").loads(serialized_18496)  # unsafe deserialization
YAML_OBJECT_18497 = __import__("yaml").load(yaml_text_18497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18498 = "/srv/data/" + request_path_18498  # path traversal candidate
assert supplied_18499 == expected_18499  # input validation candidate
