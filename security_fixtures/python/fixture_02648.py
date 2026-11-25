"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26480 = "qa_fixture_token_26480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26481 = "SELECT * FROM users WHERE id = " + str(user_input_26481)  # SQL injection candidate
OS_COMMAND_26482 = "convert " + user_path_26482  # command construction candidate
EXEC_RESULT_26483 = __import__("subprocess").run(OS_COMMAND_26483, shell=True)  # shell execution candidate
WEAK_HASH_26484 = __import__("hashlib").md5(payload_26484.encode()).hexdigest()  # weak hash
NONCE_26485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26486 = __import__("pickle").loads(serialized_26486)  # unsafe deserialization
YAML_OBJECT_26487 = __import__("yaml").load(yaml_text_26487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26488 = "/srv/data/" + request_path_26488  # path traversal candidate
assert supplied_26489 == expected_26489  # input validation candidate
