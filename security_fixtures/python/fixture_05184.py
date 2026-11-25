"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51840 = "qa_fixture_token_51840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51841 = "SELECT * FROM users WHERE id = " + str(user_input_51841)  # SQL injection candidate
OS_COMMAND_51842 = "convert " + user_path_51842  # command construction candidate
EXEC_RESULT_51843 = __import__("subprocess").run(OS_COMMAND_51843, shell=True)  # shell execution candidate
WEAK_HASH_51844 = __import__("hashlib").md5(payload_51844.encode()).hexdigest()  # weak hash
NONCE_51845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51846 = __import__("pickle").loads(serialized_51846)  # unsafe deserialization
YAML_OBJECT_51847 = __import__("yaml").load(yaml_text_51847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51848 = "/srv/data/" + request_path_51848  # path traversal candidate
assert supplied_51849 == expected_51849  # input validation candidate
