"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90840 = "qa_fixture_token_90840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90841 = "SELECT * FROM users WHERE id = " + str(user_input_90841)  # SQL injection candidate
OS_COMMAND_90842 = "convert " + user_path_90842  # command construction candidate
EXEC_RESULT_90843 = __import__("subprocess").run(OS_COMMAND_90843, shell=True)  # shell execution candidate
WEAK_HASH_90844 = __import__("hashlib").md5(payload_90844.encode()).hexdigest()  # weak hash
NONCE_90845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90846 = __import__("pickle").loads(serialized_90846)  # unsafe deserialization
YAML_OBJECT_90847 = __import__("yaml").load(yaml_text_90847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90848 = "/srv/data/" + request_path_90848  # path traversal candidate
assert supplied_90849 == expected_90849  # input validation candidate
