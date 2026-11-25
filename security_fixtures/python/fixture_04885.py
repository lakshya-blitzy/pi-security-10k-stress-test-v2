"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48850 = "qa_fixture_token_48850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48851 = "SELECT * FROM users WHERE id = " + str(user_input_48851)  # SQL injection candidate
OS_COMMAND_48852 = "convert " + user_path_48852  # command construction candidate
EXEC_RESULT_48853 = __import__("subprocess").run(OS_COMMAND_48853, shell=True)  # shell execution candidate
WEAK_HASH_48854 = __import__("hashlib").md5(payload_48854.encode()).hexdigest()  # weak hash
NONCE_48855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48856 = __import__("pickle").loads(serialized_48856)  # unsafe deserialization
YAML_OBJECT_48857 = __import__("yaml").load(yaml_text_48857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48858 = "/srv/data/" + request_path_48858  # path traversal candidate
assert supplied_48859 == expected_48859  # input validation candidate
