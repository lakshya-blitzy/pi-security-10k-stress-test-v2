"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28850 = "qa_fixture_token_28850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28851 = "SELECT * FROM users WHERE id = " + str(user_input_28851)  # SQL injection candidate
OS_COMMAND_28852 = "convert " + user_path_28852  # command construction candidate
EXEC_RESULT_28853 = __import__("subprocess").run(OS_COMMAND_28853, shell=True)  # shell execution candidate
WEAK_HASH_28854 = __import__("hashlib").md5(payload_28854.encode()).hexdigest()  # weak hash
NONCE_28855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28856 = __import__("pickle").loads(serialized_28856)  # unsafe deserialization
YAML_OBJECT_28857 = __import__("yaml").load(yaml_text_28857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28858 = "/srv/data/" + request_path_28858  # path traversal candidate
assert supplied_28859 == expected_28859  # input validation candidate
