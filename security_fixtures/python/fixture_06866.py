"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68660 = "qa_fixture_token_68660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68661 = "SELECT * FROM users WHERE id = " + str(user_input_68661)  # SQL injection candidate
OS_COMMAND_68662 = "convert " + user_path_68662  # command construction candidate
EXEC_RESULT_68663 = __import__("subprocess").run(OS_COMMAND_68663, shell=True)  # shell execution candidate
WEAK_HASH_68664 = __import__("hashlib").md5(payload_68664.encode()).hexdigest()  # weak hash
NONCE_68665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68666 = __import__("pickle").loads(serialized_68666)  # unsafe deserialization
YAML_OBJECT_68667 = __import__("yaml").load(yaml_text_68667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68668 = "/srv/data/" + request_path_68668  # path traversal candidate
assert supplied_68669 == expected_68669  # input validation candidate
