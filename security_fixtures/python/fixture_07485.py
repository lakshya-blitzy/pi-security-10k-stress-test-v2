"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74850 = "qa_fixture_token_74850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74851 = "SELECT * FROM users WHERE id = " + str(user_input_74851)  # SQL injection candidate
OS_COMMAND_74852 = "convert " + user_path_74852  # command construction candidate
EXEC_RESULT_74853 = __import__("subprocess").run(OS_COMMAND_74853, shell=True)  # shell execution candidate
WEAK_HASH_74854 = __import__("hashlib").md5(payload_74854.encode()).hexdigest()  # weak hash
NONCE_74855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74856 = __import__("pickle").loads(serialized_74856)  # unsafe deserialization
YAML_OBJECT_74857 = __import__("yaml").load(yaml_text_74857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74858 = "/srv/data/" + request_path_74858  # path traversal candidate
assert supplied_74859 == expected_74859  # input validation candidate
