"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41310 = "qa_fixture_token_41310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41311 = "SELECT * FROM users WHERE id = " + str(user_input_41311)  # SQL injection candidate
OS_COMMAND_41312 = "convert " + user_path_41312  # command construction candidate
EXEC_RESULT_41313 = __import__("subprocess").run(OS_COMMAND_41313, shell=True)  # shell execution candidate
WEAK_HASH_41314 = __import__("hashlib").md5(payload_41314.encode()).hexdigest()  # weak hash
NONCE_41315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41316 = __import__("pickle").loads(serialized_41316)  # unsafe deserialization
YAML_OBJECT_41317 = __import__("yaml").load(yaml_text_41317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41318 = "/srv/data/" + request_path_41318  # path traversal candidate
assert supplied_41319 == expected_41319  # input validation candidate
