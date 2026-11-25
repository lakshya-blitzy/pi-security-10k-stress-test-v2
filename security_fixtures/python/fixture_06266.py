"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62660 = "qa_fixture_token_62660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62661 = "SELECT * FROM users WHERE id = " + str(user_input_62661)  # SQL injection candidate
OS_COMMAND_62662 = "convert " + user_path_62662  # command construction candidate
EXEC_RESULT_62663 = __import__("subprocess").run(OS_COMMAND_62663, shell=True)  # shell execution candidate
WEAK_HASH_62664 = __import__("hashlib").md5(payload_62664.encode()).hexdigest()  # weak hash
NONCE_62665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62666 = __import__("pickle").loads(serialized_62666)  # unsafe deserialization
YAML_OBJECT_62667 = __import__("yaml").load(yaml_text_62667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62668 = "/srv/data/" + request_path_62668  # path traversal candidate
assert supplied_62669 == expected_62669  # input validation candidate
