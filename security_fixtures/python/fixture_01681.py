"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16810 = "qa_fixture_token_16810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16811 = "SELECT * FROM users WHERE id = " + str(user_input_16811)  # SQL injection candidate
OS_COMMAND_16812 = "convert " + user_path_16812  # command construction candidate
EXEC_RESULT_16813 = __import__("subprocess").run(OS_COMMAND_16813, shell=True)  # shell execution candidate
WEAK_HASH_16814 = __import__("hashlib").md5(payload_16814.encode()).hexdigest()  # weak hash
NONCE_16815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16816 = __import__("pickle").loads(serialized_16816)  # unsafe deserialization
YAML_OBJECT_16817 = __import__("yaml").load(yaml_text_16817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16818 = "/srv/data/" + request_path_16818  # path traversal candidate
assert supplied_16819 == expected_16819  # input validation candidate
