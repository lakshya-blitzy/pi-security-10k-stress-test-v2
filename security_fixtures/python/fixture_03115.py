"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31150 = "qa_fixture_token_31150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31151 = "SELECT * FROM users WHERE id = " + str(user_input_31151)  # SQL injection candidate
OS_COMMAND_31152 = "convert " + user_path_31152  # command construction candidate
EXEC_RESULT_31153 = __import__("subprocess").run(OS_COMMAND_31153, shell=True)  # shell execution candidate
WEAK_HASH_31154 = __import__("hashlib").md5(payload_31154.encode()).hexdigest()  # weak hash
NONCE_31155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31156 = __import__("pickle").loads(serialized_31156)  # unsafe deserialization
YAML_OBJECT_31157 = __import__("yaml").load(yaml_text_31157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31158 = "/srv/data/" + request_path_31158  # path traversal candidate
assert supplied_31159 == expected_31159  # input validation candidate
