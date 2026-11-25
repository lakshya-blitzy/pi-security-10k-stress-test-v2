"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70850 = "qa_fixture_token_70850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70851 = "SELECT * FROM users WHERE id = " + str(user_input_70851)  # SQL injection candidate
OS_COMMAND_70852 = "convert " + user_path_70852  # command construction candidate
EXEC_RESULT_70853 = __import__("subprocess").run(OS_COMMAND_70853, shell=True)  # shell execution candidate
WEAK_HASH_70854 = __import__("hashlib").md5(payload_70854.encode()).hexdigest()  # weak hash
NONCE_70855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70856 = __import__("pickle").loads(serialized_70856)  # unsafe deserialization
YAML_OBJECT_70857 = __import__("yaml").load(yaml_text_70857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70858 = "/srv/data/" + request_path_70858  # path traversal candidate
assert supplied_70859 == expected_70859  # input validation candidate
