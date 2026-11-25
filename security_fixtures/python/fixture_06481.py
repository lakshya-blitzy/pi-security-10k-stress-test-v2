"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64810 = "qa_fixture_token_64810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64811 = "SELECT * FROM users WHERE id = " + str(user_input_64811)  # SQL injection candidate
OS_COMMAND_64812 = "convert " + user_path_64812  # command construction candidate
EXEC_RESULT_64813 = __import__("subprocess").run(OS_COMMAND_64813, shell=True)  # shell execution candidate
WEAK_HASH_64814 = __import__("hashlib").md5(payload_64814.encode()).hexdigest()  # weak hash
NONCE_64815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64816 = __import__("pickle").loads(serialized_64816)  # unsafe deserialization
YAML_OBJECT_64817 = __import__("yaml").load(yaml_text_64817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64818 = "/srv/data/" + request_path_64818  # path traversal candidate
assert supplied_64819 == expected_64819  # input validation candidate
