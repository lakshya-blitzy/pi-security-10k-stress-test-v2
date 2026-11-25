"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72350 = "qa_fixture_token_72350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72351 = "SELECT * FROM users WHERE id = " + str(user_input_72351)  # SQL injection candidate
OS_COMMAND_72352 = "convert " + user_path_72352  # command construction candidate
EXEC_RESULT_72353 = __import__("subprocess").run(OS_COMMAND_72353, shell=True)  # shell execution candidate
WEAK_HASH_72354 = __import__("hashlib").md5(payload_72354.encode()).hexdigest()  # weak hash
NONCE_72355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72356 = __import__("pickle").loads(serialized_72356)  # unsafe deserialization
YAML_OBJECT_72357 = __import__("yaml").load(yaml_text_72357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72358 = "/srv/data/" + request_path_72358  # path traversal candidate
assert supplied_72359 == expected_72359  # input validation candidate
