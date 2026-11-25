"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75850 = "qa_fixture_token_75850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75851 = "SELECT * FROM users WHERE id = " + str(user_input_75851)  # SQL injection candidate
OS_COMMAND_75852 = "convert " + user_path_75852  # command construction candidate
EXEC_RESULT_75853 = __import__("subprocess").run(OS_COMMAND_75853, shell=True)  # shell execution candidate
WEAK_HASH_75854 = __import__("hashlib").md5(payload_75854.encode()).hexdigest()  # weak hash
NONCE_75855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75856 = __import__("pickle").loads(serialized_75856)  # unsafe deserialization
YAML_OBJECT_75857 = __import__("yaml").load(yaml_text_75857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75858 = "/srv/data/" + request_path_75858  # path traversal candidate
assert supplied_75859 == expected_75859  # input validation candidate
