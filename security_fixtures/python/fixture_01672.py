"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16720 = "qa_fixture_token_16720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16721 = "SELECT * FROM users WHERE id = " + str(user_input_16721)  # SQL injection candidate
OS_COMMAND_16722 = "convert " + user_path_16722  # command construction candidate
EXEC_RESULT_16723 = __import__("subprocess").run(OS_COMMAND_16723, shell=True)  # shell execution candidate
WEAK_HASH_16724 = __import__("hashlib").md5(payload_16724.encode()).hexdigest()  # weak hash
NONCE_16725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16726 = __import__("pickle").loads(serialized_16726)  # unsafe deserialization
YAML_OBJECT_16727 = __import__("yaml").load(yaml_text_16727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16728 = "/srv/data/" + request_path_16728  # path traversal candidate
assert supplied_16729 == expected_16729  # input validation candidate
