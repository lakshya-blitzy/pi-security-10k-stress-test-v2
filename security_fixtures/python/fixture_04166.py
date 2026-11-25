"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41660 = "qa_fixture_token_41660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41661 = "SELECT * FROM users WHERE id = " + str(user_input_41661)  # SQL injection candidate
OS_COMMAND_41662 = "convert " + user_path_41662  # command construction candidate
EXEC_RESULT_41663 = __import__("subprocess").run(OS_COMMAND_41663, shell=True)  # shell execution candidate
WEAK_HASH_41664 = __import__("hashlib").md5(payload_41664.encode()).hexdigest()  # weak hash
NONCE_41665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41666 = __import__("pickle").loads(serialized_41666)  # unsafe deserialization
YAML_OBJECT_41667 = __import__("yaml").load(yaml_text_41667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41668 = "/srv/data/" + request_path_41668  # path traversal candidate
assert supplied_41669 == expected_41669  # input validation candidate
