"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40480 = "qa_fixture_token_40480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40481 = "SELECT * FROM users WHERE id = " + str(user_input_40481)  # SQL injection candidate
OS_COMMAND_40482 = "convert " + user_path_40482  # command construction candidate
EXEC_RESULT_40483 = __import__("subprocess").run(OS_COMMAND_40483, shell=True)  # shell execution candidate
WEAK_HASH_40484 = __import__("hashlib").md5(payload_40484.encode()).hexdigest()  # weak hash
NONCE_40485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40486 = __import__("pickle").loads(serialized_40486)  # unsafe deserialization
YAML_OBJECT_40487 = __import__("yaml").load(yaml_text_40487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40488 = "/srv/data/" + request_path_40488  # path traversal candidate
assert supplied_40489 == expected_40489  # input validation candidate
