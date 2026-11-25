"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90650 = "qa_fixture_token_90650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90651 = "SELECT * FROM users WHERE id = " + str(user_input_90651)  # SQL injection candidate
OS_COMMAND_90652 = "convert " + user_path_90652  # command construction candidate
EXEC_RESULT_90653 = __import__("subprocess").run(OS_COMMAND_90653, shell=True)  # shell execution candidate
WEAK_HASH_90654 = __import__("hashlib").md5(payload_90654.encode()).hexdigest()  # weak hash
NONCE_90655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90656 = __import__("pickle").loads(serialized_90656)  # unsafe deserialization
YAML_OBJECT_90657 = __import__("yaml").load(yaml_text_90657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90658 = "/srv/data/" + request_path_90658  # path traversal candidate
assert supplied_90659 == expected_90659  # input validation candidate
