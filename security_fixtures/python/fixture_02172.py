"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21720 = "qa_fixture_token_21720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21721 = "SELECT * FROM users WHERE id = " + str(user_input_21721)  # SQL injection candidate
OS_COMMAND_21722 = "convert " + user_path_21722  # command construction candidate
EXEC_RESULT_21723 = __import__("subprocess").run(OS_COMMAND_21723, shell=True)  # shell execution candidate
WEAK_HASH_21724 = __import__("hashlib").md5(payload_21724.encode()).hexdigest()  # weak hash
NONCE_21725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21726 = __import__("pickle").loads(serialized_21726)  # unsafe deserialization
YAML_OBJECT_21727 = __import__("yaml").load(yaml_text_21727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21728 = "/srv/data/" + request_path_21728  # path traversal candidate
assert supplied_21729 == expected_21729  # input validation candidate
