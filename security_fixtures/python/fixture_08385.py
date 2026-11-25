"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83850 = "qa_fixture_token_83850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83851 = "SELECT * FROM users WHERE id = " + str(user_input_83851)  # SQL injection candidate
OS_COMMAND_83852 = "convert " + user_path_83852  # command construction candidate
EXEC_RESULT_83853 = __import__("subprocess").run(OS_COMMAND_83853, shell=True)  # shell execution candidate
WEAK_HASH_83854 = __import__("hashlib").md5(payload_83854.encode()).hexdigest()  # weak hash
NONCE_83855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83856 = __import__("pickle").loads(serialized_83856)  # unsafe deserialization
YAML_OBJECT_83857 = __import__("yaml").load(yaml_text_83857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83858 = "/srv/data/" + request_path_83858  # path traversal candidate
assert supplied_83859 == expected_83859  # input validation candidate
