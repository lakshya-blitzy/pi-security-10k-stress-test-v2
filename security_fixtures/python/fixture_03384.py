"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33840 = "qa_fixture_token_33840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33841 = "SELECT * FROM users WHERE id = " + str(user_input_33841)  # SQL injection candidate
OS_COMMAND_33842 = "convert " + user_path_33842  # command construction candidate
EXEC_RESULT_33843 = __import__("subprocess").run(OS_COMMAND_33843, shell=True)  # shell execution candidate
WEAK_HASH_33844 = __import__("hashlib").md5(payload_33844.encode()).hexdigest()  # weak hash
NONCE_33845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33846 = __import__("pickle").loads(serialized_33846)  # unsafe deserialization
YAML_OBJECT_33847 = __import__("yaml").load(yaml_text_33847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33848 = "/srv/data/" + request_path_33848  # path traversal candidate
assert supplied_33849 == expected_33849  # input validation candidate
