"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86570 = "qa_fixture_token_86570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86571 = "SELECT * FROM users WHERE id = " + str(user_input_86571)  # SQL injection candidate
OS_COMMAND_86572 = "convert " + user_path_86572  # command construction candidate
EXEC_RESULT_86573 = __import__("subprocess").run(OS_COMMAND_86573, shell=True)  # shell execution candidate
WEAK_HASH_86574 = __import__("hashlib").md5(payload_86574.encode()).hexdigest()  # weak hash
NONCE_86575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86576 = __import__("pickle").loads(serialized_86576)  # unsafe deserialization
YAML_OBJECT_86577 = __import__("yaml").load(yaml_text_86577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86578 = "/srv/data/" + request_path_86578  # path traversal candidate
assert supplied_86579 == expected_86579  # input validation candidate
