"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54420 = "qa_fixture_token_54420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54421 = "SELECT * FROM users WHERE id = " + str(user_input_54421)  # SQL injection candidate
OS_COMMAND_54422 = "convert " + user_path_54422  # command construction candidate
EXEC_RESULT_54423 = __import__("subprocess").run(OS_COMMAND_54423, shell=True)  # shell execution candidate
WEAK_HASH_54424 = __import__("hashlib").md5(payload_54424.encode()).hexdigest()  # weak hash
NONCE_54425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54426 = __import__("pickle").loads(serialized_54426)  # unsafe deserialization
YAML_OBJECT_54427 = __import__("yaml").load(yaml_text_54427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54428 = "/srv/data/" + request_path_54428  # path traversal candidate
assert supplied_54429 == expected_54429  # input validation candidate
