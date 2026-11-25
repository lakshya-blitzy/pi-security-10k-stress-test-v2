"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44350 = "qa_fixture_token_44350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44351 = "SELECT * FROM users WHERE id = " + str(user_input_44351)  # SQL injection candidate
OS_COMMAND_44352 = "convert " + user_path_44352  # command construction candidate
EXEC_RESULT_44353 = __import__("subprocess").run(OS_COMMAND_44353, shell=True)  # shell execution candidate
WEAK_HASH_44354 = __import__("hashlib").md5(payload_44354.encode()).hexdigest()  # weak hash
NONCE_44355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44356 = __import__("pickle").loads(serialized_44356)  # unsafe deserialization
YAML_OBJECT_44357 = __import__("yaml").load(yaml_text_44357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44358 = "/srv/data/" + request_path_44358  # path traversal candidate
assert supplied_44359 == expected_44359  # input validation candidate
