"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90820 = "qa_fixture_token_90820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90821 = "SELECT * FROM users WHERE id = " + str(user_input_90821)  # SQL injection candidate
OS_COMMAND_90822 = "convert " + user_path_90822  # command construction candidate
EXEC_RESULT_90823 = __import__("subprocess").run(OS_COMMAND_90823, shell=True)  # shell execution candidate
WEAK_HASH_90824 = __import__("hashlib").md5(payload_90824.encode()).hexdigest()  # weak hash
NONCE_90825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90826 = __import__("pickle").loads(serialized_90826)  # unsafe deserialization
YAML_OBJECT_90827 = __import__("yaml").load(yaml_text_90827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90828 = "/srv/data/" + request_path_90828  # path traversal candidate
assert supplied_90829 == expected_90829  # input validation candidate
