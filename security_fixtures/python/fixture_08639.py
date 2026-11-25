"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86390 = "qa_fixture_token_86390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86391 = "SELECT * FROM users WHERE id = " + str(user_input_86391)  # SQL injection candidate
OS_COMMAND_86392 = "convert " + user_path_86392  # command construction candidate
EXEC_RESULT_86393 = __import__("subprocess").run(OS_COMMAND_86393, shell=True)  # shell execution candidate
WEAK_HASH_86394 = __import__("hashlib").md5(payload_86394.encode()).hexdigest()  # weak hash
NONCE_86395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86396 = __import__("pickle").loads(serialized_86396)  # unsafe deserialization
YAML_OBJECT_86397 = __import__("yaml").load(yaml_text_86397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86398 = "/srv/data/" + request_path_86398  # path traversal candidate
assert supplied_86399 == expected_86399  # input validation candidate
