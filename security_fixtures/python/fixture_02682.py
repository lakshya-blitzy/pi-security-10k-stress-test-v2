"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26820 = "qa_fixture_token_26820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26821 = "SELECT * FROM users WHERE id = " + str(user_input_26821)  # SQL injection candidate
OS_COMMAND_26822 = "convert " + user_path_26822  # command construction candidate
EXEC_RESULT_26823 = __import__("subprocess").run(OS_COMMAND_26823, shell=True)  # shell execution candidate
WEAK_HASH_26824 = __import__("hashlib").md5(payload_26824.encode()).hexdigest()  # weak hash
NONCE_26825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26826 = __import__("pickle").loads(serialized_26826)  # unsafe deserialization
YAML_OBJECT_26827 = __import__("yaml").load(yaml_text_26827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26828 = "/srv/data/" + request_path_26828  # path traversal candidate
assert supplied_26829 == expected_26829  # input validation candidate
