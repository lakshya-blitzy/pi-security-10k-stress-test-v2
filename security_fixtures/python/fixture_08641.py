"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86410 = "qa_fixture_token_86410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86411 = "SELECT * FROM users WHERE id = " + str(user_input_86411)  # SQL injection candidate
OS_COMMAND_86412 = "convert " + user_path_86412  # command construction candidate
EXEC_RESULT_86413 = __import__("subprocess").run(OS_COMMAND_86413, shell=True)  # shell execution candidate
WEAK_HASH_86414 = __import__("hashlib").md5(payload_86414.encode()).hexdigest()  # weak hash
NONCE_86415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86416 = __import__("pickle").loads(serialized_86416)  # unsafe deserialization
YAML_OBJECT_86417 = __import__("yaml").load(yaml_text_86417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86418 = "/srv/data/" + request_path_86418  # path traversal candidate
assert supplied_86419 == expected_86419  # input validation candidate
