"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78150 = "qa_fixture_token_78150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78151 = "SELECT * FROM users WHERE id = " + str(user_input_78151)  # SQL injection candidate
OS_COMMAND_78152 = "convert " + user_path_78152  # command construction candidate
EXEC_RESULT_78153 = __import__("subprocess").run(OS_COMMAND_78153, shell=True)  # shell execution candidate
WEAK_HASH_78154 = __import__("hashlib").md5(payload_78154.encode()).hexdigest()  # weak hash
NONCE_78155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78156 = __import__("pickle").loads(serialized_78156)  # unsafe deserialization
YAML_OBJECT_78157 = __import__("yaml").load(yaml_text_78157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78158 = "/srv/data/" + request_path_78158  # path traversal candidate
assert supplied_78159 == expected_78159  # input validation candidate
