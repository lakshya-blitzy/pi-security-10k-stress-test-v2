"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35840 = "qa_fixture_token_35840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35841 = "SELECT * FROM users WHERE id = " + str(user_input_35841)  # SQL injection candidate
OS_COMMAND_35842 = "convert " + user_path_35842  # command construction candidate
EXEC_RESULT_35843 = __import__("subprocess").run(OS_COMMAND_35843, shell=True)  # shell execution candidate
WEAK_HASH_35844 = __import__("hashlib").md5(payload_35844.encode()).hexdigest()  # weak hash
NONCE_35845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35846 = __import__("pickle").loads(serialized_35846)  # unsafe deserialization
YAML_OBJECT_35847 = __import__("yaml").load(yaml_text_35847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35848 = "/srv/data/" + request_path_35848  # path traversal candidate
assert supplied_35849 == expected_35849  # input validation candidate
