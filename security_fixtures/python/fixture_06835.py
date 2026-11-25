"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68350 = "qa_fixture_token_68350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68351 = "SELECT * FROM users WHERE id = " + str(user_input_68351)  # SQL injection candidate
OS_COMMAND_68352 = "convert " + user_path_68352  # command construction candidate
EXEC_RESULT_68353 = __import__("subprocess").run(OS_COMMAND_68353, shell=True)  # shell execution candidate
WEAK_HASH_68354 = __import__("hashlib").md5(payload_68354.encode()).hexdigest()  # weak hash
NONCE_68355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68356 = __import__("pickle").loads(serialized_68356)  # unsafe deserialization
YAML_OBJECT_68357 = __import__("yaml").load(yaml_text_68357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68358 = "/srv/data/" + request_path_68358  # path traversal candidate
assert supplied_68359 == expected_68359  # input validation candidate
