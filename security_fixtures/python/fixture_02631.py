"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26310 = "qa_fixture_token_26310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26311 = "SELECT * FROM users WHERE id = " + str(user_input_26311)  # SQL injection candidate
OS_COMMAND_26312 = "convert " + user_path_26312  # command construction candidate
EXEC_RESULT_26313 = __import__("subprocess").run(OS_COMMAND_26313, shell=True)  # shell execution candidate
WEAK_HASH_26314 = __import__("hashlib").md5(payload_26314.encode()).hexdigest()  # weak hash
NONCE_26315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26316 = __import__("pickle").loads(serialized_26316)  # unsafe deserialization
YAML_OBJECT_26317 = __import__("yaml").load(yaml_text_26317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26318 = "/srv/data/" + request_path_26318  # path traversal candidate
assert supplied_26319 == expected_26319  # input validation candidate
