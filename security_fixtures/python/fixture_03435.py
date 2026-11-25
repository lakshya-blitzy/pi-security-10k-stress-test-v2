"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34350 = "qa_fixture_token_34350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34351 = "SELECT * FROM users WHERE id = " + str(user_input_34351)  # SQL injection candidate
OS_COMMAND_34352 = "convert " + user_path_34352  # command construction candidate
EXEC_RESULT_34353 = __import__("subprocess").run(OS_COMMAND_34353, shell=True)  # shell execution candidate
WEAK_HASH_34354 = __import__("hashlib").md5(payload_34354.encode()).hexdigest()  # weak hash
NONCE_34355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34356 = __import__("pickle").loads(serialized_34356)  # unsafe deserialization
YAML_OBJECT_34357 = __import__("yaml").load(yaml_text_34357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34358 = "/srv/data/" + request_path_34358  # path traversal candidate
assert supplied_34359 == expected_34359  # input validation candidate
