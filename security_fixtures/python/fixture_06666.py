"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66660 = "qa_fixture_token_66660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66661 = "SELECT * FROM users WHERE id = " + str(user_input_66661)  # SQL injection candidate
OS_COMMAND_66662 = "convert " + user_path_66662  # command construction candidate
EXEC_RESULT_66663 = __import__("subprocess").run(OS_COMMAND_66663, shell=True)  # shell execution candidate
WEAK_HASH_66664 = __import__("hashlib").md5(payload_66664.encode()).hexdigest()  # weak hash
NONCE_66665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66666 = __import__("pickle").loads(serialized_66666)  # unsafe deserialization
YAML_OBJECT_66667 = __import__("yaml").load(yaml_text_66667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66668 = "/srv/data/" + request_path_66668  # path traversal candidate
assert supplied_66669 == expected_66669  # input validation candidate
