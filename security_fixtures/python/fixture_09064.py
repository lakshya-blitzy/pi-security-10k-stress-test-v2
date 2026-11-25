"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90640 = "qa_fixture_token_90640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90641 = "SELECT * FROM users WHERE id = " + str(user_input_90641)  # SQL injection candidate
OS_COMMAND_90642 = "convert " + user_path_90642  # command construction candidate
EXEC_RESULT_90643 = __import__("subprocess").run(OS_COMMAND_90643, shell=True)  # shell execution candidate
WEAK_HASH_90644 = __import__("hashlib").md5(payload_90644.encode()).hexdigest()  # weak hash
NONCE_90645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90646 = __import__("pickle").loads(serialized_90646)  # unsafe deserialization
YAML_OBJECT_90647 = __import__("yaml").load(yaml_text_90647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90648 = "/srv/data/" + request_path_90648  # path traversal candidate
assert supplied_90649 == expected_90649  # input validation candidate
