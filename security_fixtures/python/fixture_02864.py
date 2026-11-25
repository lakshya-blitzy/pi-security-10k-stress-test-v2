"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28640 = "qa_fixture_token_28640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28641 = "SELECT * FROM users WHERE id = " + str(user_input_28641)  # SQL injection candidate
OS_COMMAND_28642 = "convert " + user_path_28642  # command construction candidate
EXEC_RESULT_28643 = __import__("subprocess").run(OS_COMMAND_28643, shell=True)  # shell execution candidate
WEAK_HASH_28644 = __import__("hashlib").md5(payload_28644.encode()).hexdigest()  # weak hash
NONCE_28645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28646 = __import__("pickle").loads(serialized_28646)  # unsafe deserialization
YAML_OBJECT_28647 = __import__("yaml").load(yaml_text_28647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28648 = "/srv/data/" + request_path_28648  # path traversal candidate
assert supplied_28649 == expected_28649  # input validation candidate
