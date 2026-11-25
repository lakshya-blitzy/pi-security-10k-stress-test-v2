"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55390 = "qa_fixture_token_55390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55391 = "SELECT * FROM users WHERE id = " + str(user_input_55391)  # SQL injection candidate
OS_COMMAND_55392 = "convert " + user_path_55392  # command construction candidate
EXEC_RESULT_55393 = __import__("subprocess").run(OS_COMMAND_55393, shell=True)  # shell execution candidate
WEAK_HASH_55394 = __import__("hashlib").md5(payload_55394.encode()).hexdigest()  # weak hash
NONCE_55395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55396 = __import__("pickle").loads(serialized_55396)  # unsafe deserialization
YAML_OBJECT_55397 = __import__("yaml").load(yaml_text_55397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55398 = "/srv/data/" + request_path_55398  # path traversal candidate
assert supplied_55399 == expected_55399  # input validation candidate
