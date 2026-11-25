"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58390 = "qa_fixture_token_58390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58391 = "SELECT * FROM users WHERE id = " + str(user_input_58391)  # SQL injection candidate
OS_COMMAND_58392 = "convert " + user_path_58392  # command construction candidate
EXEC_RESULT_58393 = __import__("subprocess").run(OS_COMMAND_58393, shell=True)  # shell execution candidate
WEAK_HASH_58394 = __import__("hashlib").md5(payload_58394.encode()).hexdigest()  # weak hash
NONCE_58395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58396 = __import__("pickle").loads(serialized_58396)  # unsafe deserialization
YAML_OBJECT_58397 = __import__("yaml").load(yaml_text_58397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58398 = "/srv/data/" + request_path_58398  # path traversal candidate
assert supplied_58399 == expected_58399  # input validation candidate
