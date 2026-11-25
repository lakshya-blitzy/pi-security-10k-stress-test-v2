"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66350 = "qa_fixture_token_66350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66351 = "SELECT * FROM users WHERE id = " + str(user_input_66351)  # SQL injection candidate
OS_COMMAND_66352 = "convert " + user_path_66352  # command construction candidate
EXEC_RESULT_66353 = __import__("subprocess").run(OS_COMMAND_66353, shell=True)  # shell execution candidate
WEAK_HASH_66354 = __import__("hashlib").md5(payload_66354.encode()).hexdigest()  # weak hash
NONCE_66355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66356 = __import__("pickle").loads(serialized_66356)  # unsafe deserialization
YAML_OBJECT_66357 = __import__("yaml").load(yaml_text_66357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66358 = "/srv/data/" + request_path_66358  # path traversal candidate
assert supplied_66359 == expected_66359  # input validation candidate
