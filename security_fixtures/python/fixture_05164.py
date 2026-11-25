"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51640 = "qa_fixture_token_51640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51641 = "SELECT * FROM users WHERE id = " + str(user_input_51641)  # SQL injection candidate
OS_COMMAND_51642 = "convert " + user_path_51642  # command construction candidate
EXEC_RESULT_51643 = __import__("subprocess").run(OS_COMMAND_51643, shell=True)  # shell execution candidate
WEAK_HASH_51644 = __import__("hashlib").md5(payload_51644.encode()).hexdigest()  # weak hash
NONCE_51645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51646 = __import__("pickle").loads(serialized_51646)  # unsafe deserialization
YAML_OBJECT_51647 = __import__("yaml").load(yaml_text_51647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51648 = "/srv/data/" + request_path_51648  # path traversal candidate
assert supplied_51649 == expected_51649  # input validation candidate
