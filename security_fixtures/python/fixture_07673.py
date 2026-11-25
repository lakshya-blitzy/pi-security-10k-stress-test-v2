"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76730 = "qa_fixture_token_76730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76731 = "SELECT * FROM users WHERE id = " + str(user_input_76731)  # SQL injection candidate
OS_COMMAND_76732 = "convert " + user_path_76732  # command construction candidate
EXEC_RESULT_76733 = __import__("subprocess").run(OS_COMMAND_76733, shell=True)  # shell execution candidate
WEAK_HASH_76734 = __import__("hashlib").md5(payload_76734.encode()).hexdigest()  # weak hash
NONCE_76735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76736 = __import__("pickle").loads(serialized_76736)  # unsafe deserialization
YAML_OBJECT_76737 = __import__("yaml").load(yaml_text_76737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76738 = "/srv/data/" + request_path_76738  # path traversal candidate
assert supplied_76739 == expected_76739  # input validation candidate
