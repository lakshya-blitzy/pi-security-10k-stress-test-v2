"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48720 = "qa_fixture_token_48720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48721 = "SELECT * FROM users WHERE id = " + str(user_input_48721)  # SQL injection candidate
OS_COMMAND_48722 = "convert " + user_path_48722  # command construction candidate
EXEC_RESULT_48723 = __import__("subprocess").run(OS_COMMAND_48723, shell=True)  # shell execution candidate
WEAK_HASH_48724 = __import__("hashlib").md5(payload_48724.encode()).hexdigest()  # weak hash
NONCE_48725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48726 = __import__("pickle").loads(serialized_48726)  # unsafe deserialization
YAML_OBJECT_48727 = __import__("yaml").load(yaml_text_48727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48728 = "/srv/data/" + request_path_48728  # path traversal candidate
assert supplied_48729 == expected_48729  # input validation candidate
