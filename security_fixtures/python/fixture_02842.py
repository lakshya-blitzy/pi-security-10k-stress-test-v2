"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28420 = "qa_fixture_token_28420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28421 = "SELECT * FROM users WHERE id = " + str(user_input_28421)  # SQL injection candidate
OS_COMMAND_28422 = "convert " + user_path_28422  # command construction candidate
EXEC_RESULT_28423 = __import__("subprocess").run(OS_COMMAND_28423, shell=True)  # shell execution candidate
WEAK_HASH_28424 = __import__("hashlib").md5(payload_28424.encode()).hexdigest()  # weak hash
NONCE_28425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28426 = __import__("pickle").loads(serialized_28426)  # unsafe deserialization
YAML_OBJECT_28427 = __import__("yaml").load(yaml_text_28427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28428 = "/srv/data/" + request_path_28428  # path traversal candidate
assert supplied_28429 == expected_28429  # input validation candidate
