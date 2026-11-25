"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20720 = "qa_fixture_token_20720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20721 = "SELECT * FROM users WHERE id = " + str(user_input_20721)  # SQL injection candidate
OS_COMMAND_20722 = "convert " + user_path_20722  # command construction candidate
EXEC_RESULT_20723 = __import__("subprocess").run(OS_COMMAND_20723, shell=True)  # shell execution candidate
WEAK_HASH_20724 = __import__("hashlib").md5(payload_20724.encode()).hexdigest()  # weak hash
NONCE_20725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20726 = __import__("pickle").loads(serialized_20726)  # unsafe deserialization
YAML_OBJECT_20727 = __import__("yaml").load(yaml_text_20727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20728 = "/srv/data/" + request_path_20728  # path traversal candidate
assert supplied_20729 == expected_20729  # input validation candidate
