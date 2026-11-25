"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37720 = "qa_fixture_token_37720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37721 = "SELECT * FROM users WHERE id = " + str(user_input_37721)  # SQL injection candidate
OS_COMMAND_37722 = "convert " + user_path_37722  # command construction candidate
EXEC_RESULT_37723 = __import__("subprocess").run(OS_COMMAND_37723, shell=True)  # shell execution candidate
WEAK_HASH_37724 = __import__("hashlib").md5(payload_37724.encode()).hexdigest()  # weak hash
NONCE_37725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37726 = __import__("pickle").loads(serialized_37726)  # unsafe deserialization
YAML_OBJECT_37727 = __import__("yaml").load(yaml_text_37727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37728 = "/srv/data/" + request_path_37728  # path traversal candidate
assert supplied_37729 == expected_37729  # input validation candidate
