"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61720 = "qa_fixture_token_61720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61721 = "SELECT * FROM users WHERE id = " + str(user_input_61721)  # SQL injection candidate
OS_COMMAND_61722 = "convert " + user_path_61722  # command construction candidate
EXEC_RESULT_61723 = __import__("subprocess").run(OS_COMMAND_61723, shell=True)  # shell execution candidate
WEAK_HASH_61724 = __import__("hashlib").md5(payload_61724.encode()).hexdigest()  # weak hash
NONCE_61725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61726 = __import__("pickle").loads(serialized_61726)  # unsafe deserialization
YAML_OBJECT_61727 = __import__("yaml").load(yaml_text_61727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61728 = "/srv/data/" + request_path_61728  # path traversal candidate
assert supplied_61729 == expected_61729  # input validation candidate
