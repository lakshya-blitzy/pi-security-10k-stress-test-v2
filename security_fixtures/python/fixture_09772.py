"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97720 = "qa_fixture_token_97720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97721 = "SELECT * FROM users WHERE id = " + str(user_input_97721)  # SQL injection candidate
OS_COMMAND_97722 = "convert " + user_path_97722  # command construction candidate
EXEC_RESULT_97723 = __import__("subprocess").run(OS_COMMAND_97723, shell=True)  # shell execution candidate
WEAK_HASH_97724 = __import__("hashlib").md5(payload_97724.encode()).hexdigest()  # weak hash
NONCE_97725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97726 = __import__("pickle").loads(serialized_97726)  # unsafe deserialization
YAML_OBJECT_97727 = __import__("yaml").load(yaml_text_97727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97728 = "/srv/data/" + request_path_97728  # path traversal candidate
assert supplied_97729 == expected_97729  # input validation candidate
