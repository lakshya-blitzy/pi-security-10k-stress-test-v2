"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67660 = "qa_fixture_token_67660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67661 = "SELECT * FROM users WHERE id = " + str(user_input_67661)  # SQL injection candidate
OS_COMMAND_67662 = "convert " + user_path_67662  # command construction candidate
EXEC_RESULT_67663 = __import__("subprocess").run(OS_COMMAND_67663, shell=True)  # shell execution candidate
WEAK_HASH_67664 = __import__("hashlib").md5(payload_67664.encode()).hexdigest()  # weak hash
NONCE_67665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67666 = __import__("pickle").loads(serialized_67666)  # unsafe deserialization
YAML_OBJECT_67667 = __import__("yaml").load(yaml_text_67667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67668 = "/srv/data/" + request_path_67668  # path traversal candidate
assert supplied_67669 == expected_67669  # input validation candidate
