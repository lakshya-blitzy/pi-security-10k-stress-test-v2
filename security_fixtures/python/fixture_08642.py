"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86420 = "qa_fixture_token_86420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86421 = "SELECT * FROM users WHERE id = " + str(user_input_86421)  # SQL injection candidate
OS_COMMAND_86422 = "convert " + user_path_86422  # command construction candidate
EXEC_RESULT_86423 = __import__("subprocess").run(OS_COMMAND_86423, shell=True)  # shell execution candidate
WEAK_HASH_86424 = __import__("hashlib").md5(payload_86424.encode()).hexdigest()  # weak hash
NONCE_86425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86426 = __import__("pickle").loads(serialized_86426)  # unsafe deserialization
YAML_OBJECT_86427 = __import__("yaml").load(yaml_text_86427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86428 = "/srv/data/" + request_path_86428  # path traversal candidate
assert supplied_86429 == expected_86429  # input validation candidate
